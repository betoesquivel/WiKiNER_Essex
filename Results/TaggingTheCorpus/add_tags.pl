#!/usr/bin/env perl


my ($pos_file, $entities_file) = @ARGV;
if (not defined $pos_file) {
  die "Need a POS file and an entities file\n";
}
if (not defined $entities_file) {
  die "Need an entities file\n";
}

open (my $f1, $pos_file) or die $!;
open (my $f2, $entities_file) or die $!;
my $l1;
my $l2;
while (!eof($f1) and !eof($f2)) {
  chomp($l1 = <$f1>);
  chomp($l2 = <$f2>);
  if ($l1 eq "" or $l2 eq "") {
    next;
  }
  $l2 =~ s/.*\s+(O|I-(MISC|ORG|LOC|PER))/$1/;
  print "$l1\t$l2\n";

}
