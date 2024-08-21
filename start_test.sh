#!/bin/bash
# need chmod +
sudo docker compose up;
sudo docker stop $(sudo docker ps -a -q);
sudo docker rm $(sudo docker ps -a -q);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^backend_for_bike_rental_service_picasso_diagnostic-django_api" | cut -d' ' -f2);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^backend_for_bike_rental_service_picasso_diagnostic-celery_worker" | cut -d' ' -f2);
sudo rm -r dump/;