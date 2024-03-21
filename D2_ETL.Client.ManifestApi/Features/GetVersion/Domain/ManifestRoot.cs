using System.Text.Json.Serialization;

namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Domain;

public class ManifestRoot<TResponse> where TResponse : class
{
    public TResponse? Response { get; init; }
}