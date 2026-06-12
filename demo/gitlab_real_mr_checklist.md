# GitLab Real MR Demo Checklist

Use this checklist once a GitLab project is available.

## A. Prepare project

- [ ] Use the dedicated GitLab Transcend project if provisioned.
- [ ] If not provisioned yet, use a temporary personal GitLab project for rehearsal only.
- [ ] Do not store tokens in the repository.
- [ ] Keep the project public or accessible to judges when appropriate.

## B. Create demo MR

- [ ] Start with `demo/invoice_app_before` as the clean baseline.
- [ ] Create a branch named `demo/controller-model-bypass`.
- [ ] Apply the bad controller change from `demo/invoice_app_after_bad_mr`.
- [ ] Open a Merge Request.
- [ ] Use MR title: `Demo: bypass service layer in invoice creation`.
- [ ] Use the description from `demo/mr_description.md`.

## C. Run agent

- [ ] Run tests locally: `python -m pytest -q`.
- [ ] Run mock mode and regenerate `demo/sample_mr_comment.md`.
- [ ] Run GitLab API dry-run against the MR.
- [ ] Confirm the endpoint points to the expected project/MR.
- [ ] Export `GITLAB_TOKEN` locally.
- [ ] Run GitLab API live mode.
- [ ] Confirm the MR comment appears.

## D. Capture evidence

- [ ] Screenshot: MR diff showing direct `InvoiceModel::create` call.
- [ ] Screenshot: posted Orbit Guardrail Agent comment.
- [ ] Redacted run log saved under `demo/evidence/` if used in submission.
- [ ] Update Devpost Try It Out links.
- [ ] Record demo video using `demo/video_shot_list.md`.

## E. Pending GitLab Transcend final compliance

- [ ] Replace rehearsal project with dedicated hackathon project if required.
- [ ] Connect to GitLab Orbit API/CLI/skill interface.
- [ ] Wrap or expose as GitLab Duo agent/flow/skill.
- [ ] Publish final agent/flow/skill to AI Catalog.
