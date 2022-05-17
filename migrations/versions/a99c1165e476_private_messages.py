"""private messages

Revision ID: a99c1165e476
Revises: 9db4f46dd61b
Create Date: 2022-05-16 02:06:43.851991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a99c1165e476'
down_revision = '9db4f46dd61b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_message_read_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_message_read_time')
    # ### end Alembic commands ###