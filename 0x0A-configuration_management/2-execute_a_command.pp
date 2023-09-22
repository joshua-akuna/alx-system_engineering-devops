# creates a manifest that kills a process name killmenow
exec{'killmenow':
  command     => 'pkill -f "killmenow"',
  onlyif      => 'pgrep -f "killmenow"',
  provider    => shell,
  refresh     => true
}
