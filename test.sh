#! bin/bash
pytest ./service_one
pytest ./service_two
pytest --cov application ./service_one
pytest --cov application ./service_two

