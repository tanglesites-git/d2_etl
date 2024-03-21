using System.Text.Json;
using D2_ETL.Client.ManifestApi.Common;
using D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Domain;
using D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Requests;
using D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Response;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Domain;
using FluentValidation;

namespace D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage;

public static class GetMobileWorldContentPathsByLanguageEndpoint
{
    public static void MapGetMobileWorldContentPathsByLanguage(this WebApplication app, HttpSettings httpSettings)
    {
        app.MapGet("manifest/{language}/world_content_database",
            async (ManifestLanguage language, IValidator<ManifestLanguage> validator) =>
            {
                var validationResult = await validator.ValidateAsync(language);

                if (!validationResult.IsValid)
                {
                    return Results.BadRequest(validationResult.Errors);
                }

                var content =
                    await System.IO.File.ReadAllTextAsync(Path.Combine(httpSettings?.RootDirectory!, "manifest.json"));
                var manifest = JsonSerializer.Deserialize<ManifestRoot<MobileWorldContentPaths>>(content);

                if (manifest?.Response?.mobileWorldContentPaths is null)
                {
                    return Results.Problem();
                }

                return language.language switch
                {
                    "en" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.en!)),
                    "fr" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.fr!)),
                    "es" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.es!)),
                    "de" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.de!)),
                    "it" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.it!)),
                    "ja" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.ja!)),
                    "pt-br" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.pt_br!)),
                    "es-mx" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.es_mx!)),
                    "ru" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.ru!)),
                    "pl" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.pl!)),
                    "zh-cht" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.zh_cht!)),
                    "zh-chs" => Results.Ok(
                        new MobileWorldContentPathsResponse(manifest?.Response?.mobileWorldContentPaths?.zh_chs!)),
                    _ => Results.NotFound()
                };
            });
    }
}