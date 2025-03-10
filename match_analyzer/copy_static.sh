# Copy CSS from staticfiles to static directory
if [ -d "staticfiles/analysis/css" ]; then
  cp -r staticfiles/analysis/css/* static/analysis/css/
elif [ -d "match_analyzer/analysis/static/analysis/css" ]; then
  cp -r match_analyzer/analysis/static/analysis/css/* static/analysis/css/
elif [ -d "analysis/static/analysis/css" ]; then
  cp -r analysis/static/analysis/css/* static/analysis/css/
fi
