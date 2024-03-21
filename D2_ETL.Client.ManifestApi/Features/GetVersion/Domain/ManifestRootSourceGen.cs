using System.Text.Json.Serialization;

namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Domain;

[JsonSerializable(typeof(ManifestRoot<ManifestVersion>))]
public partial class ManifestRootSourceGen : JsonSerializerContext
{
    
}