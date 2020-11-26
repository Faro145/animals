#! bin/bash
docker tag service_one rfarq75/service_one
docker tag service_two rfarq75/service_two
docker push rfarq75/service_one
docker push rfarq75/service_two
