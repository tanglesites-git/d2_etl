using System.Text.Json.Serialization.Metadata;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Domain;

namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Interfaces;

public interface IManifestJsonSerializer
{
    public TResponse? Deserialize<TResponse>(string content, JsonTypeInfo<TResponse> jsonTypeInfo)
        where TResponse : class;
}