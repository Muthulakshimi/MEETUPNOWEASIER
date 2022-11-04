 **<h1 align="center"> MEETUPSNOWEASIER </h1>**
 
>_<h2> MADE FOR THE ORGANISERS 😊</h2>_


**<h3>The end goal: To make the job of announcing an event easier for the organisers in every level with just one click!!!</h3>**

**<p>Problem Statement with solution:** We got the idea of making the process of organising the event easier through AWS, everytime the organiser plans an event he'll have to make the announcement in every social media available to get the concentrated crowd from all sources hence this idea of one-click announcement popped up!! In here all the organiser has got to do is to post his plan for event with some description such as his name, e-mail id, message and picture related to his event and with one-click he'll get it posted in all platforms...(as shown in the website pic) </p>

 <a href="https://drive.google.com/uc?export=view&id=1EvMae5_I3bT-1cQRadajsKUjmjHOy0sX"><img src="https://drive.google.com/uc?export=view&id=1EvMae5_I3bT-1cQRadajsKUjmjHOy0sX" style="width: 650px; max-width: 100%; height: auto" title="Click to access picture" />

 <p>Later the organiser can start checking up the posts done via our website in specific social medias, for this we'd have collected all the details of the organiser beforehand and we'll store it in our database. We'll work on showing the collection of details of the organiser using frontend in the future. Till date we have slack, discord, instagram, twitter and mail up and running successfully. Once the details are entered by the user one can start off checking if the posts are successfully made as it'll be taken care by our website!! </p>
  
 <a href="https://drive.google.com/uc?export=view&id=1EuiEi7uDJ6WXDC8-GF7WvHPuMptxWL_H"><img src="https://drive.google.com/uc?export=view&id=1EuiEi7uDJ6WXDC8-GF7WvHPuMptxWL_H" style="width: 650px; max-width: 100%; height: auto" title="Click to access picture" />
  
  
**<p>How have we used AWS:** We have used AWS Lambda to initiate email module as shown below in the webpage pic. We'd be including the other social media API's using lambda in the future. We have triggered this feature with the API Gateway which uses Rest API, then we run the Lambda service in response to events tp automatically manage the computing resources needed by it to execute the mail. </p>
  
  <a href="https://drive.google.com/uc?export=view&id=1EwvkeNA76gT2UdtejzDOMJLgdc3ez0zl"><img src="https://drive.google.com/uc?export=view&id=1EwvkeNA76gT2UdtejzDOMJLgdc3ez0zl" style="width: 650px; max-width: 100%; height: auto" title="Click to access picture" />
