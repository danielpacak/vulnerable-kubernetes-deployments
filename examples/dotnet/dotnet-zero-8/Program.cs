using System.Globalization;
using System.Formats.Asn1;
using dotnet_zero;
using Newtonsoft.Json;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var logger = app.Logger;

int RollDice()
{
    return Random.Shared.Next(1, 7);
}

string HandleRollDice(string? player)
{
    var result = RollDice();

    if (string.IsNullOrEmpty(player))
    {
        logger.LogInformation("Anonymous player is rolling the dice: {result}", result);
    }
    else
    {
        logger.LogInformation("{player} is rolling the dice: {result}", player, result);
    }

    return result.ToString(CultureInfo.InvariantCulture);
}

string HandleSomeFun()
{
    var writer = new AsnWriter(AsnEncodingRules.DER);

    using (writer.PushSequence())
    {
        writer.WriteInteger(1);

        writer.WriteObjectIdentifier("2.16.840.1.101.3.4.2.1");
    }

    var value = writer.Encode();

    return Convert.ToBase64String(value);
}

string HandlePerson()
{
    Person person = new Person();
    person.FirstName = "John";
    person.LastName = "Doe";
    return JsonConvert.SerializeObject(person);
}

app.MapGet("/healtz", () => Results.Ok("OK"));
app.MapGet("/rolldice/{player?}", HandleRollDice);
app.MapGet("/somefun", HandleSomeFun);
app.MapGet("/person", HandlePerson);

app.Run();