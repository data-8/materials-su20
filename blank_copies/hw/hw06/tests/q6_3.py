test = {
  'name': 'q6_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(just_apples_given_apples, float)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> (just_apples_given_apples >= 0) & (just_apples_given_apples <= 1)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
