using System.Text.Json;
using D2_ETL.Client.ManifestApi.Common;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Interfaces;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Query;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Response;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Domain;
using MediatR;

namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Handlers;

public class ManifestVersionHandler : IRequestHandler<ManifestVersionQuery, IResult>
{
    private readonly IManifestIO _manifestIO;
    private readonly IManifestJsonSerializer _manifestJsonSerializer;
    public ManifestVersionHandler(IManifestIO manifestIo, IManifestJsonSerializer manifestJsonSerializer)
    {
        _manifestIO = manifestIo;
        _manifestJsonSerializer = manifestJsonSerializer;
    }
    public async Task<IResult> Handle(ManifestVersionQuery request, CancellationToken cancellationToken)
    {
        var content = await _manifestIO.ReadAllTextAsync(Path.Combine(request.GetRootDirectory(), MagicStrings.ManifestFilename), cancellationToken);
        var manifest = _manifestJsonSerializer.Deserialize(content, ManifestRootSourceGen.Default.ManifestRootManifestVersion);
        return Results.Ok(new ManifestVersionResponse(manifest?.Response?.version));
    }
}