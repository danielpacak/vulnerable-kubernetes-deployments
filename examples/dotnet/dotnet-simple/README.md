# dotnet-simple

```
dotnet build
```

```
dotnet run
```

Open http://localhost:8080/rolldice


```
docker buildx build --push --platform linux/amd64,linux/arm64 -t danielpacak/dotnet-simple:10 -f Dockerfile .
```

``` console
$ dotnet new list web
These templates matched your input: 'web'

Template Name                                 Short Name    Language  Tags                      
--------------------------------------------  ------------  --------  --------------------------
ASP.NET Core Empty                            web           [C#],F#   Web/Empty                 
ASP.NET Core Web API                          webapi        [C#],F#   Web/Web API/API/Service   
ASP.NET Core Web API (native AOT)             webapiaot     [C#]      Web/Web API/API/Service   
ASP.NET Core Web App (Model-View-Controller)  mvc           [C#],F#   Web/MVC                   
ASP.NET Core Web App (Razor Pages)            webapp,razor  [C#]      Web/MVC/Razor Pages       
Blazor Web App                                blazor        [C#]      Web/Blazor/WebAssembly    
Blazor WebAssembly Standalone App             blazorwasm    [C#]      Web/Blazor/WebAssembly/PWA
Web Config                                    webconfig               Config                    
```

``` console
$ k gadget run trace_open -n dotnet-simple --output columns --fields fname | grep -i OpenTelemetry
/app/OpenTelemetry.dll          
/app/OpenTelemetry.Extensions.H…
/app/OpenTelemetry.Api.Provider…
/app/OpenTelemetry.Api.dll      
/app/OpenTelemetry.Instrumentat…
/app/OpenTelemetry.Exporter.Con…
```

## Further Reading

* https://opentelemetry.io/docs/languages/dotnet/getting-started/
* https://opentelemetry.io/docs/zero-code/dotnet/
* https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api?view=aspnetcore-10.0&tabs=visual-studio
* https://learn.microsoft.com/en-us/dotnet/core/docker/build-container?tabs=linux&pivots=dotnet-10-0
* https://learn.microsoft.com/en-us/dotnet/core/containers/sdk-publish
* https://learn.microsoft.com/en-us/dotnet/core/docker/introduction
* https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api?view=aspnetcore-10.0&tabs=visual-studio-code
