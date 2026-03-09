FROM --platform=${BUILDPLATFORM} mcr.microsoft.com/dotnet/sdk:10.0 AS builder
ARG TARGETARCH
ARG BUILD_CONFIGURATION=Release

WORKDIR /src
COPY . ./
RUN dotnet restore "./dotnet-simple.csproj" -r linux-$TARGETARCH
RUN dotnet build "./dotnet-simple.csproj" -r linux-$TARGETARCH -c $BUILD_CONFIGURATION -o /app/build

FROM builder AS publish
ARG TARGETARCH
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./dotnet-simple.csproj" -r linux-$TARGETARCH -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:10.0
USER app
WORKDIR /app
COPY --from=publish /app/publish .
EXPOSE 8080

ENTRYPOINT ["dotnet", "dotnet-simple.dll"]
