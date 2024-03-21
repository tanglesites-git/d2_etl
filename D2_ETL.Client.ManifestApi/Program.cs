using D2_ETL.Client.ManifestApi.Common;
using D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Requests;
using D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Validation;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Application;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Application.Interfaces;
using D2_ETL.Client.ManifestApi.Features.GetVersion.Infrastructure;
using FluentValidation;

var builder = WebApplication.CreateBuilder(args);

var httpSettings = builder.Configuration.GetSection("HttpSettings").Get<HttpSettings>();

builder.Services.Configure<HttpSettings>(builder.Configuration.GetSection(HttpSettings.SectionName));

builder.Services.AddTransient<IManifestIO, ManifestIO>();
builder.Services.AddTransient<IManifestJsonSerializer, ManifestJsonSerializer>();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddMediatR(options =>
{
    options.RegisterServicesFromAssembly(typeof(Program).Assembly);
});
builder.Services.AddTransient<IValidator<ManifestLanguage>, LanguageValidator>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapGetManifestVersion();
// app.MapGetMobileWorldContentPathsByLanguage(httpSettings!);

app.Run();