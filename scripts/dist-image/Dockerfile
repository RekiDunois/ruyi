# syntax=docker/dockerfile:1
FROM --platform=linux/amd64 ubuntu:20.04 AS build-amd64
FROM --platform=linux/arm64 ubuntu:20.04 AS build-arm64
FROM --platform=linux/riscv64 riscv64/ubuntu:22.04 AS build-riscv64

FROM build-$TARGETARCH

ARG TARGETARCH
ARG BUILDER_UID=1000
ARG BUILDER_GID=1000

COPY ./prepare-distro.sh ./prepare-distro.*.sh /tmp/
RUN /tmp/prepare-distro.sh $TARGETARCH

COPY ./prepare-poetry.sh /tmp/prepare-poetry.sh
RUN /tmp/prepare-poetry.sh

USER $BUILDER_UID:$BUILDER_GID
WORKDIR /home/b
