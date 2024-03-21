namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Interfaces;

public interface IManifestIO
{
    Task<string> ReadAllTextAsync(string path, CancellationToken cancellationToken);
}