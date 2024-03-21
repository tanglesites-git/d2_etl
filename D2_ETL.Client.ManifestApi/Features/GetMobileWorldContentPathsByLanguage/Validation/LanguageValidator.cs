using D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Requests;
using FluentValidation;

namespace D2_ETL.Client.ManifestApi.Features.GetMobileWorldContentPathsByLanguage.Validation;

public class LanguageValidator : AbstractValidator<ManifestLanguage>
{
    public LanguageValidator()
    {
        RuleFor(x => x.language)
            .NotNull()
            .NotEmpty()
            .WithMessage("Language is required");
        RuleFor(x => x.language)
            .Must(x => x is "en" or "fr" or "es" or "de" or "it" or "ja" or "pt-br" or "es-mx" or "ru" or "pl"
                or "zh-cht" or "zh-chs")
            .WithMessage("Language is not valid");
    }
}