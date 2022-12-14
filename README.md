# YogaSite

Problem Statement:-

Assume that you are the CTO for the outsourcing firm which has been chosen to build an
admission form for the Yoga Classes which happen every month.
Requirements for the admission form are:

- Only people within the age limit of 18-65 can enroll for the monthly classes and they will
be paying the fees on a month on month basis. I.e. an individual will have to pay the fees
every month and he can pay it any time of the month.

- They can enroll any day but they will have to pay for the entire month. The monthly fee is
500/- Rs INR.

- There are a total of 4 batches a day namely 6-7AM, 7-8AM, 8-9AM and 5-6PM. The
participants can choose any batch in a month and can move to any other batch next
month. I.e. participants can shift from one batch to another in different months but in
same month they need to be in same batch



My Implementation:-

I developed a Django app is a responsive website for the individual customers to use and help them to keep track of their payment transactions along with the chosen batch of current date. Every customers can access their data and make new transactions only after being autorised through passwords. 

-The basic model behind this project is a Customer model which has its objects as a specific customer. And this model contains the data and information about the name, age, email, password, batch, payment date.

-Once a user is registered, its object gets created along with all the details.

-When a user want to login to their profile, it demands a password and matches the same with the password already stored in the database.

-There is an another model of Payment which is simply a transaction having start date, end date, batch and balance. This model has a Foreign Key user_of_payment which, it uses to connect with the individual customers who are making the transaction. And that's how all the payment transactions (objects of Payments model) are associated with any specific user.

-Hence, with my solution and approach, the models are less and the data is stored in a very structured way and organised way.

-With the making of every Payment object (Payment transaction) with the help of the function CompletePayment(), the balance gets updated in the profile page and the customer can have a track of their past transactions along with the total time. 

-The frontend basically contributes in making all the required validations.

-Although, the name and username of any two users cannot be same as they are unique contraints. The age also have a limited range between 18 and 65.


ER Diagram:-
