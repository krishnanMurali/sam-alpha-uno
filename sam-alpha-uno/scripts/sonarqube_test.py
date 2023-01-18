#!/usr/bin/python
import logging
from sonarqube import SonarQubeClient

url = "http://localhost:9000"
user_name = "admin"
pwd = "password123"


def main():
    logging.info("starting the connection\n")
    sonar = SonarQubeClient(sonarqube_url=url, username=user_name, password=pwd)
    component = sonar.measures.get_component_with_specified_measures(
        component="sam-alpha-uno",
        branch="main",
        fields="metrics,periods",
        metricKeys="code_smells,bugs",
    )
    print(component)


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s INFO: %(message)s", level=logging.INFO)
    main()
