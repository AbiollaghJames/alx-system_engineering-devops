#!/usr/bin/env ruby
puts ARGV[0].scan(/\[sender:(\+?\w+)\] \[receiver:(\+?\w+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/).join(",")
