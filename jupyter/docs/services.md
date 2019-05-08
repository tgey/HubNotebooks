# Services

The projects uses the following technologies :


[Docker]: https://www.docker.com/
[docker-compose]: https://docs.docker.com/compose/
[Python 3.7]: https://www.python.org/downloads/release/python-370/
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[Neo4j]: https://neo4j.com/
[JupyterLab]: https://jupyterlab.readthedocs.io/en/stable/
[Doccano]: https://doccano.herokuapp.com/
[Grafana]: https://grafana.com/
[Prometheus]: https://prometheus.io/
[cAdvisor]: https://github.com/google/cadvisor/blob/master/README.md
[Node-Exporter]: https://github.com/prometheus/node_exporter
[AlertManager]: https://prometheus.io/docs/alerting/alertmanager/
[Traefik]: https://traefik.io/

| Services                      | Description                           | Route                     |
| ----------------------------- | ------------------------------------- | --------------------------|
| [Docker] (& [docker-compose]) | application isolation from root system| X                         |
| [Python 3.7] ([PEP8] standard)| main language                         | X                         |
| [Neo4J]                       | Graph database                        | neo4j.localhost           |
| [JupyterLab]                  | IDE for notebooks                     | jupyter.localhost         |
| [Doccano]                     | Annotation tool                       | doccano.localhost         |
| [Grafana]                     | Graphic metrics monitor               | grafana.localhost         |
| [Prometheus]                  | metrics manager                       | prometheus.localhost      |
| [cAdvisor]                    | container metrics                     | cadvisor.localhost        |
| [Node-Exporter]               | machine metrics                       | nodeexporter.localhost    |
| [AlertManager]                | alert handler                         | alertmanager.localhost    |
| [Traefik]                     | Edge Router & Reverse Proxy           | localhost:8080            |