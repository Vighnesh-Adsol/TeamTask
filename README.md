# TaskView


## #-About
**TeamTask** is a web application made for group project management, which includes adding tasks and jobs according to the groups job allocation.
This helps in understanding and managing the chronology of the project sub-tasks so that every member of the group can handle their own side with admiration.

This was the team effort made possible by combining the ideas and technical understanding of me & my peers.

## #-Why This Idea?
The answer of this question can differ from other perspectives but from my side, I think some groups like mine sometime doesn't understand the overly complicated technologies such as git and GitHub for project management. We tend to work along with the flow where the only complicated thing we work with is our own code. I agree that git and GitHub are really appreciable technologies, I like using them too. But my concern is there maybe people who don't understand such techsavy stuff. And along with that, they might not hae the time to learn all that while learning their tech stack. This concludes the reason for the website. 

## #-How To Run this project on local Machine:

### Step I:
#### Recommended:
Fork this repo so that you have a copy of your own on your GitHub and then paste this in your terminal (change <Your-account-name> with your account name) -

```shell
git clone https://github.com/<Your-account-name>/TeamTask.git
```
#### Or else:
directly paste this terminal command in the directory you want this project into -
```shell
git clone https://github.com/Vighnesh-Adsol/TeamTask.git
```

### Step II:
Confirm that you are into **crm** directory where the **manage.py** is loctated. or just paste this command in terminal -
```shell
cd crm
```

###  Step III:
- Firstly we need to make the migration here so paste this in terminal -
```shell
python manage.py makemigrations
```
- After making migrations we need to actually migrate the file so that the models and forms created can be generated in the database as well therefore -
```shell
python manage.py migrate
```
- Now Finally we can run the server on our localHost by running -
```shell
python manage.py runserver
```
now by pressing control + clicking on the http link it will launch the browser with our website.
