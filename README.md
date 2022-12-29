# REChase-2022

Online treasure hunt

Install virtualenvironment (if not already)

```
pip install virtualenv
virtualenv myenv
```

Activate virtualenv

```
myenv\scripts\activate
```

> PS : Linux Users follow different guidelines
> For further details refer <a href="https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/">https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/


Fast starting up quickly, do

```
chmod +x startUp.sh
./startUp.sh
```

or run the commands

```
# Install requirements
pip install -r ../requirements.txt

# Make a .env file(will overwrite existing one)
cp .env.example .env

# Run loadData.sh
sudo chmod +x loadData.sh
./loadData.sh

# Run server
python manage.py runserver
```

Commands to dump existing data:

```
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 4 > {filename}.json
```

Command to load the existing data:

```
python manage.py loaddata {filename}.json
```

PS- Just replace {filename} with the name you want to give.
