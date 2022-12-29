pip install -r ../requirements.txt
cp .env.example .env
sudo chmod +x loadData.sh
./loadData.sh
python manage.py runserver
