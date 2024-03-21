namespace D2_ETL.Client.ManifestApi.Common;

public class HttpSettings
{
    public const string SectionName = "HttpSettings";
    public string? BaseAddress { get; init; }
    public string? ApiKey { get; init; }
    public string? ManifestUrl { get; init; }
    public string? RootDirectory { get; init; }
}