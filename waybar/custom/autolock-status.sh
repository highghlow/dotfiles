while [ 1 ]; do

  if ps -e | grep swayidle > /dev/null; then
    echo '{"text": "LCK: active", "class": ["alock-active", "alock-status"]}'
  else
    echo '{"text": "LCK: stopped", "class": ["alock-stopped", "alock-status"]}'
  fi
  sleep 1

done;
