# Protocol limitations and deviations

The intended condition blinding was incomplete. Original notes in two released packages (isolation-A and backpropagation-A) explicitly described the assigned skill as old. Path/filename masking caught old-skill but missed the prose phrase old skill. The judge reported the isolation-A leak during review. Already released packages were preserved; no scores or rubric changed. Later package masking also removes old/new skill wording. Treat this as an independent artifact audit with partial blinding, not a fully blinded experiment. Graph schemas and histories may reveal workflow in any case.

The file observer samples graph writes every two seconds. It preserves observed initial/intermediate/final states but can miss rapid writes; absence of an observed intermediate does not prove fabricated history. Worker-saved history and available observed states must be assessed together.
