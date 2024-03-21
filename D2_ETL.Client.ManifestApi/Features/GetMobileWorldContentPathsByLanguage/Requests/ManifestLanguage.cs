namespace D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Requests;


public class ManifestLanguage : IParsable<ManifestLanguage>
{
    public string? language { get; set; }

    public static ManifestLanguage Parse(string s, IFormatProvider? provider)
    {
        return new ManifestLanguage { language = s };
    }

    static bool IParsable<ManifestLanguage>.TryParse(string? s, IFormatProvider? provider, out ManifestLanguage result)
    {
        result = new ManifestLanguage { language = s };
        return true;
    }
}