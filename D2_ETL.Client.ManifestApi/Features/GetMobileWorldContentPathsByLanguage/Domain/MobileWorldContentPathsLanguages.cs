using System.Text.Json.Serialization;

namespace D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Domain;

public class MobileWorldContentPathsLanguages
{
    public string? en { get; set; }
    public string? fr { get; set; }
    public string? es { get; set; }
    public string? de { get; set; }
    public string? it { get; set; }
    public string? ja { get; set; }
    [JsonPropertyName("pt-br")]
    public string? pt_br { get; set; }
    [JsonPropertyName("es-mx")]
    public string? es_mx { get; set; }
    public string? ru { get; set; }
    public string? pl { get; set; }
    [JsonPropertyName("zh-cht")]
    public string? zh_cht { get; set; }
    [JsonPropertyName("zh-chs")]
    public string? zh_chs { get; set; }
}