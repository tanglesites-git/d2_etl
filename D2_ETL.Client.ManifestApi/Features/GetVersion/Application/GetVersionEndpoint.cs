using D2_ETL.Client.ManifestApi.Common;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Query;
using MediatR;
using Microsoft.Extensions.Options;

namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Application;

public static class GetVersionEndpoint
{
    public static void MapGetManifestVersion(this WebApplication app)
    {
        app.MapGet("manifest/version", async (IMediator mediator, IOptionsMonitor<HttpSettings> HttpSettings) =>
        {
            var query = new ManifestVersionQuery(HttpSettings);
            return await mediator.Send(query);
        });
    }
}