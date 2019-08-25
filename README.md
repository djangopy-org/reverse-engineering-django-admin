# Guide to implement Reverse Engineering of the Django Admin Foreign Key's Add/Edit Button
This is the example project for implementing Reverse Engineering of the Django Admin Foreign Key's Add/Edit Button. You can find guide from [here](https://djangopy.org/how-to/reverse-engineering-of-the-django-admin-foreign-keys-addedit-button/)



### Installation guide
- Clone repository

	`
	git clone https://github.com/djangopy-org/reverse-engineering-django-admin
	`

- cd to repository.

- Create a virtualenv by following command
	- **For Linux/Mac**
	
		`
		virtualenv -p python3 .
		`

	- **For Windows**

		`
			virtualenv .
		`

- Activate virtualenv

	- **For Linux/Mac**
	
		`
			source bin/activate
		`

	- **For Windows**

		`
			.\Scripts\activate
		`

- Install required packages

	- **For Linux/Mac**
		
		`
			pip3 install -r requirements.txt
		`

	- **For Windows**

		`
			pip install -r requirements.txt
		`

- cd to src and run the server
	
	- **For Linux/Mac**
		
		`
			python3 manage.py runserver
		`

	- **For Windows**

		`
			python manage.py runserver
		`
