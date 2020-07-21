# Websiteproj
RBS INDIA JULY HACHATHON 2020

# alphainterface
Readme File for the Website based API project Debt Buddy: 

Contains Background, Customer Value, Benefit for the Bank, Unique features, Web Application Setup instructions and links details 
(contains testing instructions and specific use cases at point 8 (i to viii) below for all the links and APIs in the APIs section)

Background:

Customer Value:
1) The Debt Buddy programme will help in assisting the Customer to become Financially aware, once we know who such customers are, it will be 
in tune with associating a debt buddy with the Customer for them to benefit further. 
2) A Wellness Survey will also help the Debt Buddy to be more aware of the customer's current financial wellness as per the customer's provided
rating (from 1 to 5).
3) The Wellness Provider API will help Vulnerable customer informing the bank only about what urgent medicinal needs. (Unique Add-ons)
4) The internal Credit Scores will further help debt buddy to engage with the customer for the right requirements. 

Benefit for the Bank:
1) Debt Buddy: The charges to the associated debt buddy will not be levied instantly but with a delay of 1 year, so that the customers who are unable to pay now
can realise the benefit of the debt buddy programme and can then pay for this. Will help in sustaining existing customers for long.
An existing customer for a longer time frame will far more be beneficial to the bank. 
So, a focus on our existing customers wellbeing and wellness will go a long way in building the Trust with the Customers.
2) WellnessProvider API will help the customers in their immediate financial needs, this will enhance the Trust and Advocacy factor with the customers.

It is a web based application utilising interfacing with oone of the existing RBS Sandbox Test API for the Accounts to provide the details if the customer's account is healthy 
or needs a debt buddy by calculating the difference of the closing balance and the initial balance as per the records for the first Account-id. 
The prototype can further be extended to include the debt buddy calculations for all other account-ids' balances.

Three APIs were also Created those are demonstrated in the above app. Those APIs are:
	1) Wellbeingsurvey for the Debt Buddy - Wellbeing 
	2) Wellnessprovider: an external API for medical stores - For Wellness Support (UNIQUE)
	3) Internal Credit Score (0,1) (that can be viewed by Debt Buddy)


Web Application setup instructions:
1) Install python For Windows from python.org/download
2) Set advanced system properties to include environment variable as PYTHON_HOME and from there edit the path to include ;%PYTHON_HOME%
3) Download Pycharm Community version from Jetbrains.com for Windows (64 bit)
4) Open Pycharm, from Pycharm's terminal install Django using command 'pip install Django'
5) Open the project (Download from Github):
from the repository alphainterface, download the folder and paste the folder Websiteproj and put into your PycharmProjects folder in the PC.
6) From terminal, goto DEMOProject directory first (i.e. CD DEMOProject) after going to Websiteproj
7) Run the runserver command: 'python manage.py runserver'

8) Click the link to view the Website project with the following features and links:
   i) Alpha Interface (home page link): (after clicking scroll down) Containing the details of the various functionalities and features like:
	a) Using Existing API for RBS Account: Account and Balances information retrieved by accessing RBS Test Sandbox API and test data initially provided to the participants
	b) Debt Buddy information retrieved with the balances in the accounts displayed
	c) finding if the customer needs debt buddy - displaying message if the final balance 
	c) Display of the Account Ids associated with the customer after the Customer number is entered
	c) Inclusion of charges details added a year from now.
	d) A NEW API created for external purpose: Wellness Support For vulnerable customers by collecting there medicinal needs that can be passed to a Wellness Provider(medical store) through an API
	e) A NEW API created: Wellness Survey for the customers participating in debt buddy programme
	f) A NEW API created: for internal CreditScore (0 and 1 flags)
   ii) Admin link: after clicking, need to enter User Id and Password. The basic user id and pwd is admin to start viewing the DEMOApp Users and the 3 New App specific details
	The authentication used across the APPS is 'Basic Auth'
	Can click on the link View Site (right top side of the panel) to go back to site.
   iii) Debtbuddy 
	Direct link: will explain the details of the Debtbuddy programme and allow to enroll directly via filling the wellbeing survey.
	
	(RBS Sandbox API): CMA9: Account API is utilised to fetch the data. 
	Customer Numbers (tests): 
		Invalid Customer Number Use Case 1: The customer number if invalid or not present in the SANDBOX test data, will fetch the error message on the screen. 
		Healthy account Use Case 2:  117707657380, after submit you will view the healthy account message on the next screen. 
				Also, available will be Account ids fetched via the APIs from the SANDBOX test data.
				At the bottom of the page, you will view the complete balance level information for the first Account-id.
		Debt Buddy elligbile Use Case 3: 234759246217, after submit you will view the Debt Buddy programme elligible message on the next screen.
	Can try with other Customer numbers also that are present in the SANDBOX test data, there are no hard-coding of the customer numbers.
	The criteria for the Debtbuddy is that the final closing account balance is more than the initial opening balance for the first Account-id 
	in this prototype. The code is scalable to cover the other Account-ids transactions for a full fledged solution after the prototype. 

   iv) Wellbeing Survey link: This survey is accessible from the iii) point above after the Use Cases 2 and 3 are tested, there will be 
	a button to enroll that will lead to wellbeing survey link. 
	The information submitted is captured, can be used for financial wellbeing later also as an API.
	If there is an error while submitting, run the migrations as follows:
		python manage.py makemigrations (check that it runs ok if not resolve the conflicts) - this is a standard makemigrations command of python.
		python manage.py migrate	(check that it runs ok if not resolve the conflicts) - this is a standard makemigrations command of python.	
	The API is built in the tool and the details will be provided in the API section below.
	This is also accessible from the Wellbeing Survey link on the top of the Web page.

    v) Wellness Support: At times, our customers are in need for urgent medicinal support. From their wellness perspective, we have created a web page form
	to capture their data. All this data, can be referred by an external wellness provider i.e. a medical store, who will be authorized to access our API via Basic Auth. 
	The API is built in the tool and the details will be provided in the API section below.

  APIs Section:

    vi)	WellnessProvider(Newly created API): This contains the details of the medicine support required by our customers as per the data received in point v) above.
	This API will be used by the authorized external wellness provider to provide the medicines directly to the customers. 
	The API uses GET Method and is supported by basic Auth. 
	It can also be run in Postman by providing the Authorization(Type: basic auth) username MedicineAuth password alphainterface
	The URL is http://127.0.0.1:8000/viewcontacts/		[note: viewcontacts/ in the URL is the EndPoint]
    vii) InternalCreditScore (Newly Created API): This is an internal score (of 0 and 1) depending on the balance status of the customers as 
	found in iii) above if it is a healthy account or Debt Buddy elligible.
    viii) WellnessSurvey (Newly Created API): This is the data of the survey, API of which can be further used to provide Debt Buddy programme elligibility.


Unique features:
	Wellness Support API that can be directly provided to the authorized medical store, Wellbeing survey [Overa and above the debt buddy]
	Website based application. With using existing API, creating a new API to provide to Wellbeing provider. and a wellbeing survey API for debt buddy consultant.

To move from Test to Prod:
	"Ensure the Client id Client Password and the Domain are appropriately provided Separately"

