FROM --platform=${BUILDPLATFORM} mcr.microsoft.com/dotnet/sdk:8.0 AS builder
ARG TARGETARCH
ARG BUILD_CONFIGURATION=Release

WORKDIR /src
COPY . ./
RUN dotnet restore "./dotnet-zero-8.csproj" -r linux-$TARGETARCH
RUN dotnet build "./dotnet-zero-8.csproj" -r linux-$TARGETARCH -c $BUILD_CONFIGURATION -o /app/build

FROM builder AS publish
ARG TARGETARCH
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./dotnet-zero-8.csproj" -r linux-$TARGETARCH -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:8.0

WORKDIR /app
COPY --from=publish /app/publish .
EXPOSE 8080

ENTRYPOINT ["dotnet", "dotnet-zero-8.dll"]
