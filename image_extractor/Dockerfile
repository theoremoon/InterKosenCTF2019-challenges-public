FROM ruby:2.5

ADD challenge /
RUN gem install bundler
RUN bundle install
CMD bundle exec ruby main.rb -o 0.0.0.0
