FROM --platform=${BUILDPLATFORM} mcr.microsoft.com/dotnet/sdk:9.0 AS builder
ARG TARGETARCH
ARG BUILD_CONFIGURATION=Release

WORKDIR /src
COPY . ./
RUN dotnet restore "./dotnet-zero-9.csproj" -r linux-$TARGETARCH
RUN dotnet build "./dotnet-zero-9.csproj" -r linux-$TARGETARCH -c $BUILD_CONFIGURATION -o /app/build

FROM builder AS publish
ARG TARGETARCH
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./dotnet-zero-9.csproj" -r linux-$TARGETARCH -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:9.0

WORKDIR /app
COPY --from=publish /app/publish .
EXPOSE 8080

ENTRYPOINT ["dotnet", "dotnet-zero-9.dll"]
