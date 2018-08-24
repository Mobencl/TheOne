# TheOne
Développement web


# This part is done except for the middlewares
# The account part:
* Registration form for the partner and the player/done
* login /logout /done
* There are going to be two middlewares: One for the partner and one for the normal user(the player) to deny access 
to some pages for each user  --It should be done the last two weeks before the presentation--

# For the partner:
* He can add Terrains with a photo for each terrain/done
* Show The terrains for the partner/done
* A partner can delete one of his terrains/done
* I can show the availibility form so the user can add availibilities but I'm still working on saving that into the database /done
* Show availibilities to the partner /done


# For the user:(Functions)/All done

--this should be done this week 4 august--
* Start Booking/ done
* Show Sportcenters with details/done
* Show Terrains of each sportcenter with availibilities/done but I still can't display the date and the time from the datetimefield/done
* make a booking(conditions for Booking in progress):there is only one booking in progress/a player cannot have two bookings in progress 
Two models : /Booking/(deleted) and Booking_inprogress   - Only one model-Booking_inprogress /DONE



# This part is what it should be done till the end of the internship/All done except the payment part //complexe in my case: multiple senders(the players), multiple receiver(me and the sportcenter)==should be chained (I receive the money and a part of the money is send to the sportcenter account)


* When a user starts a booking and doesn't finish it, he should be able to finish it wihout having to redo all the process == Working on it 
*The new availibility of the terrain is saved intothe database for every terrain/DONE



-- This should  after the internship if I don't finish the booking in progress part./DONE
* Add guests to the booking(I'm going to create an other class called Guests(Still thinking about that) /DONE


--Nouveaux objectifs--
change the widgets for the datetimefiels/not done
Add a condition so a user can't have the same availibility time for the terrains/not done yet


* Paiement plateform  // Only in theory/ Didn't have time with the new features I added the membership model because the price of the reservation changes with the memebership type :Student member/member/non member


# TheOne-New feature: 
*Invite friends to the booking_inprogress
*Membership/memebership proposal/If the user has already a membership with the sport center, he can add it to his account.
*A partner checks the membership proposal information of the player/ He can accept it or decline it.
The booking price changes in fucntion of the memebership type, the number of players who booked the terrain and the terrainType

# In the code I created a class called AIvailibility(it is supposed to be Availibility) ==didn't change it cause it was everywhere in the code, I didn't want to take the risk and change the class name.

