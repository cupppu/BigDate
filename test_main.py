hour_test = 6
if not args.hr:
    hr = convertMonDayHr(hour_test)
elif hour_test < 12:
    hr = convertMonDayHr(hour_test)
    hr = "上午" + hr
elif hour_test > 12:
    hr = convertMonDayHr(hour_test - 12)
    hr = "下午" + hr
else:
    hr = convertMonDayHr(hour_test)
    hr = "下午" + hr