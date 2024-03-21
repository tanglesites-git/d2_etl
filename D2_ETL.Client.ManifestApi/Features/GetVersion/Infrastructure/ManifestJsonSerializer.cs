using System.Text.Json;
using System.Text.Json.Serialization.Metadata;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Interfaces;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Domain;

namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Infrastructure;

public class ManifestJsonSerializer : IManifestJsonSerializer
{
    public TResponse? Deserialize<TResponse>(string content, JsonTypeInfo<TResponse> jsonTypeInfo) where TResponse : class
    {
        return JsonSerializer.Deserialize(content, jsonTypeInfo);
    }
}