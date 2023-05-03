#!/usr/bin/env ruby
puts ARGV[0].scan(/\[sender:(\+?\d+)\] \[receiver:(\+?\d+)\] \[flags:(-?\w:-?\w:-?\w:-?\w:-?\w)\]/).join(",")
