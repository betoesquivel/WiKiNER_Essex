#!/usr/bin/env perl

use strict;
use warnings;

my @words;

if (scalar @ARGV < 1) {
  die "Not enough arguments!";
}

open (my $inFile, '<', $ARGV[0]) or die $!;

my $largest_cols = 0;
while (<$inFile>) {
  chomp;
  @words = split /\s+/;
  foreach my $word (@words) {
    my $cols = $word =~ s/\|/\t/g;
    $largest_cols = $cols > $largest_cols ? $cols : $largest_cols;
    #$cols != $largest_cols ? print 'Diff!!!' : 0;
    print "$word\n";
  }
  print "\n";
}
close ($inFile);

# Just making sure that all cols are the same size.
#print $largest_cols+1;
