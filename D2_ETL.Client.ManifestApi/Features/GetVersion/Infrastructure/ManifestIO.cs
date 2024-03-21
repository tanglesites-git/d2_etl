using D2_ETL.Client.ManifestApi.Common;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Interfaces;
using Microsoft.Extensions.Options;

namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Infrastructure;

public class ManifestIO : IManifestIO
{
    public async Task<string> ReadAllTextAsync(string path, CancellationToken cancellationToken)
    {
        return await File.ReadAllTextAsync(path, cancellationToken);
    }
}