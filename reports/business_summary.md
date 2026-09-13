
# Loan Approval Disparity Analysis — Business Summary

## Business Question

Which applicant profiles are more likely to be approved or rejected for a loan, and are
there any concerning disparities across financial or demographic segments?

## Method

Analyzed 4,269 loan applications, comparing approval and rejection rates across credit
score (CIBIL), education level, self-employment status, number of dependents, annual
income, and requested loan amount.

## Key Findings

1. **CIBIL score is overwhelmingly the dominant factor in approval decisions.** Applicants
   with a "Poor" credit score (under 500) were approved only 10.7% of the time, while
   those with "Good" or "Excellent" scores (650+) were approved over 99% of the time.
   Average CIBIL score was 703.5 for approved applicants vs. 429.5 for rejected — a gap
   of 274 points.
2. **Income and loan amount show almost no independent effect on approval.** Average
   annual income was nearly identical between approved ($5.03M) and rejected ($5.11M)
   applicants; average loan amount was also nearly identical ($15.25M vs $14.95M).
   Rejected applicants were not, on average, requesting larger loans or earning less —
   they simply had substantially lower credit scores.
3. **No meaningful disparity found across education, self-employment, or number of
   dependents.** Approval rates varied by less than 1 percentage point across Graduate
   vs. Not Graduate applicants (62.5% vs 62.0%) and Self-Employed vs. not (62.2% vs
   62.2%). Approval rates across 0–5 dependents stayed within a tight 60–64% band with
   no clear trend.

## Interpretation

This lender's approval process appears to be driven almost entirely by a single hard
financial metric — credit score — rather than income, loan size, education, employment
type, or family size. From a fairness perspective, this is a reassuring pattern: the
factors that show no disparity (education, employment status, dependents) are exactly
the kind of demographic-adjacent factors that would raise concern if they *did* show a
gap. The factor that does show a massive gap (credit score) is a legitimate,
risk-relevant financial metric.

One nuance worth flagging: a small number of applicants with high credit scores (750+)
were still rejected, and a small number with lower scores were still approved,
indicating other unmeasured factors occasionally override the credit score threshold.

## Recommendation

- Applicants and advisors should treat credit score as the primary lever for approval
  likelihood — improving credit score above the ~650 threshold appears far more impactful
  than adjusting requested loan amount.
- The lender may want to investigate the small set of high-score rejections and
  low-score approvals as edge cases, to confirm those decisions were made on legitimate
  additional grounds (e.g., existing debt, employment verification issues) rather than
  inconsistent policy application.

## Limitations

- This dataset does not include the applicant's existing debt obligations, employment
  history length, or reason for the loan, all of which likely factor into real lending
  decisions.
- Correlation between credit score and approval does not by itself explain the lender's
  internal decision logic (e.g., a hard cutoff vs. a weighted scoring model) — this
  analysis identifies the pattern, not the mechanism.
