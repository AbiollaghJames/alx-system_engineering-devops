#!/usr/bin/env ruby
puts ARGV[0].scan(/\[sender:(\+?\d+)\] \[receiver:(\+?\d+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/).join(",")
