#!/usr/bin/env perl

while (<STDIN>) {
  chomp();
  $_ =~ s/\s+(O|I-(MISC|ORG|LOC|PER))//;
  print "$_\n";
  if ($_ eq "") {
    print "";
    next;
  }

}
