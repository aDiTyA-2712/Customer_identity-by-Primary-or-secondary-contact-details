from django.shortcuts import render
from .models import PrimCont
from .serializers import PrimConSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from django.utils import timezone
from rest_framework.decorators import api_view
# Create your views here.   #project =contact_service=contact ,app=contacts=contactApp,Contact=PrimCont

def truncate_string(s, max_length):
    return s[:max_length]

class PrimContListViewPost(APIView):
    def post(self,request,*args,**kwargs):
        data=request.data
        email=data.get('email')
        phone=data.get('phoneNumber')

        '''if email:
            email = truncate_string(email, 50) 
        if phone:
            phone= truncate_string(phone, 50)'''

        if not email and not phone:
            return Response({"Error":"Both can't be null, provide either fields"},status=status.HTTP_400_BAD_REQUEST)

        contacts = PrimCont.objects.filter(Q(emails=email) | Q(phones=phone)) 
                                            #emails,phones from PrimCont

        if not contacts.exists():
            primary_contact=PrimCont.objects.create(
                emails=email,
                phones=phone,
                link_precedence=PrimCont.PRIMARY,
                createdAt=timezone.now(),
                updatedAt=timezone.now()
            )
            response_data={
                "contact":{
                    "primaryContatctId": primary_contact.id,
                    "emails": [primary_contact.emails] if  primary_contact.emails else [],
                    "phoneNumbers": [primary_contact.phones] if primary_contact.phones else [],
                    "secondaryContactIds": []

                }
            }
            return Response(response_data,status=status.HTTP_200_OK)

        primary_contact=contacts.filter(link_precedence='primary').first()

        if not primary_contact:
            primary_contact=contacts.first()
            primary_contact.link_precedence=PrimCont.PRIMARY
            primary_contact.save()
        
        secondary_contacts=contacts.exclude(id=primary_contact.id)
        secondary_contact_ids=list(secondary_contacts.values_list('id',flat=True))

        emailz = [primary_contact.emails] + list(secondary_contacts.values_list('emails', flat=True))
        phone_numberz = [primary_contact.phones] + list(secondary_contacts.values_list('phones', flat=True))

        '''response_data = {
            "contact": {
                "primaryContatctId": primary_contact.id,
                "emails": [email for email in emailz if email],
                "phoneNumbers": [phone for phone in phone_numberz if phone],
                "secondaryContactIds": secondary_contact_ids
            }
        }'''#change

        if email and not contacts.filter(emails=email).exists():
            new_secondary_contact=PrimCont.objects.create(
                emails=email,
                phones=phone,
                linked_id=primary_contact.id,
                link_precedence=PrimCont.SECONDARY,
                createdAt=timezone.now(),
                updatedAt=timezone.now()
            )
            secondary_contact_ids.append(new_secondary_contact.id)
            emailz.append(new_secondary_contact.emails)
            phone_numberz.append(new_secondary_contact.phones)

        if phone and not contacts.filter(phones=phone).exists():
            new_secondary_contact=PrimCont.objects.create(
                emails=email,
                phones=phone,
                linked_id=primary_contact.id,
                link_precedence=PrimCont.SECONDARY,
                createdAt=timezone.now(),
                updatedAt=timezone.now()
            )
            secondary_contact_ids.append(new_secondary_contact.id)
            emailz.append(new_secondary_contact.emails)
            phone_numberz.append(new_secondary_contact.phones)

        primary_contact.emails=emailz
        primary_contact.phones=phone_numberz
        primary_contact.save()    

        for contact in secondary_contacts:
            if contact.link_precedence==PrimCont.PRIMARY:
                contact.link_precedence=PrimCont.SECONDARY
                contact.linked_id=primary_contact.id
                contact.save()

        response_data = {
            "contact": {
                "primaryContatctId": primary_contact.id,
                "emails": [email for email in emailz if email],
                "phoneNumbers": [phone for phone in phone_numberz if phone],
                "secondaryContactIds": secondary_contact_ids
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
@api_view(['GET'])   
def PrimContListViewGet(ListAPIView):    
    query=PrimCont.objects.all()         #same mail, diff phn and diff phone ,same mail
    serializer=PrimConSerializer(query,many=True)    #condition working in db but throwing 500 in postman
    return Response(serializer.data)