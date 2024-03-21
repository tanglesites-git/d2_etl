using D2_ETL.Client.ManifestApi.Common;
using MediatR;
using Microsoft.Extensions.Options;

namespace D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Query;

public record ManifestVersionQuery : IRequest<IResult>
{
    private readonly IOptionsMonitor<HttpSettings> _httpSettings;
    public ManifestVersionQuery(IOptionsMonitor<HttpSettings> httpSettings)
    {
        _httpSettings = httpSettings;
    }
    
    public string GetRootDirectory()
    {
        return _httpSettings?.CurrentValue.RootDirectory!;
    }
}