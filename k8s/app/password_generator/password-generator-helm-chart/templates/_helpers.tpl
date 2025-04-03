{{- define "password-generator.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "password-generator.labels" -}}
app: {{ .Chart.Name }}
release: {{ .Release.Name }}
{{- end -}}

{{- define "password-generator.service.name" -}}
{{ .Release.Name }}-{{ .Chart.Name }}-service
{{- end -}}