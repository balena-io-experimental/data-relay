FROM balenalib/%%BALENA_MACHINE_NAME%%-alpine-python:3-build as build  
# Install dapr CLI
RUN wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash
https://github.com/dapr/dapr/releases/download/v1.0.1/daprd_linux_amd64.tar.gz

# Install daprd
ARG DAPR_BUILD_DIR
COPY $DAPR_BUILD_DIR /opt/dapr
ENV PATH="/opt/dapr/:${PATH}"

# Install your app
WORKDIR /app
COPY . .
COPY . .
RUN pip install requests
ENTRYPOINT ["dapr"]
CMD ["run", "--components-path", "/app/components", "--app-id", "cloudapp", "--app-port", "3000", "python", "main.py"]